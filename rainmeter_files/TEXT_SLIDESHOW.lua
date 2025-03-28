local quoteTable = {}
local currentIndex = 1
local currentQuoteIndex = 1
local indexList = {}
local file_path
local deleted_files_path

-- Function to read a file with UTF-8 encoding
local function readFileUTF8(filepath)
    local lines = {}
    local file = io.open(filepath, "r")
    if file then
        for line in file:lines() do
            table.insert(lines, line)
        end
        file:close()
    end
    return lines
end

-- Function to load quotes and keywords
function Initialize()
    quoteTable = {}
    TimeThreshold = tonumber(SKIN:GetVariable('TimeThreshold')) or 2
    -- Global variable to track the last time CopyFilePath was called
    lastCopyTime = 0
    file_path = SKIN:GetVariable('TextPreset')
    

    local entry = ""
    for line in io.lines(SKIN:MakePathAbsolute(file_path)) do
        if line == "" then
            if entry ~= "" then
                table.insert(quoteTable, entry)
                entry = ""
            end
        else
            if entry == "" then
                entry = line
            else
                entry = entry .. "\n" .. line
            end
        end
    end

    if entry ~= "" then
        table.insert(quoteTable, entry)
    end

    indexList = {}
    for i = 1, #quoteTable do
        table.insert(indexList, i)
    end

    math.randomseed(os.time())
    for i = #indexList, 2, -1 do
        local j = math.random(i)
        indexList[i], indexList[j] = indexList[j], indexList[i]
    end

    currentIndex = 1
    currentQuoteIndex = indexList[currentIndex]
end




function legacy_CopySentence()
    -- Get the current sentence using the new extraction function
    local Sentence, _ = extractSentenceAndMetadata(quoteTable[currentQuoteIndex]) 

    -- Remove all curly brackets from the sentence
    Sentence = Sentence:gsub("[{}]", "")
    
    -- Add two linebreaks
    Sentence = Sentence .. "\n\n"

    -- Copy the cleaned sentence to the clipboard
    SKIN:Bang('!SetClip', Sentence)

    -- Update the last copy time
    lastCopyTime = os.clock()
end


------------------------------
-------RICH TEXT COPY---------
------------------------------



-- Helper function to parse color string from ini format
function parseColor(colorStr)
    local r, g, b = colorStr:match("(%d+),%s*(%d+),%s*(%d+)")
    return tonumber(r), tonumber(g), tonumber(b)
end

function createColorTable()
    local colors = {}
    for i = 1, 9 do
        local colorVar = SKIN:GetVariable('BracketColor' .. i)
        local r, g, b = parseColor(colorVar)
        -- Store the colors in a dictionary with keys as 'Color' followed by the index
        colors['Color' .. i] = {r = r, g = g, b = b}
    end
    return colors
end

function CopySentence()
    local currentTime = os.clock()
    if currentTime - lastCopyTime >= TimeThreshold then
        -- Get the current sentence using the new extraction function
        local Sentence, _ = extractSentenceAndMetadata(quoteTable[currentQuoteIndex]) 
        

        -- Create the color table
        local colors = createColorTable()

        -- Build string with colors
        local colorData = ""
        for i = 1, 9 do
            local colorVar = 'Color' .. i
            local color = colors[colorVar]
            if color then
                colorData = colorData .. colorVar .. ":" .. color.r .. "," .. color.g .. "," .. color.b .. ";"
            end
        end

        local text_color = SKIN:GetVariable('FontColor')

        -- Prepare data string with modified sentence
        local dataString = Sentence .. "||" .. "Text_color:" .. text_color .. "," .. colorData

        -- Write to temp file and execute
        local tempFilePath = SKIN:GetVariable('Temp_file_path')
        local app_path = SKIN:GetVariable('App_path')

        local file = io.open(tempFilePath, "w")
        if file then
            file:write(dataString)
            file:close()
        else
            SKIN:Bang('!Log', 'Error opening file for writing: ' .. tempFilePath)
            return
        end

        local command = '"' ..'"' .. app_path .. '"'.. " rich_text_copy -temp_file_path " .. '"' .. tempFilePath .. '"'..'"'
        SKIN:Bang('!Log', 'Command : ' .. command)
        os.execute(command)

        lastCopyTime = os.clock()
    else
        SKIN:Bang('!Log', 'Cannot copy: CopyFilePath was used less than ' .. TimeThreshold .. ' seconds ago.', 'Warning')
    end
end
------------------------------
-----RICH TEXT COPY END-------
------------------------------



function CloseSlideshow()
    -- Get the current time
    local currentTime = os.clock()

    -- Check if at least 2 second has passed since CopySentence was called
    if currentTime - lastCopyTime >= TimeThreshold then
        -- Close the slideshow
        SKIN:Bang('!DeactivateConfig')
    else
        -- Log a message or notify the user that closing is not allowed yet
        SKIN:Bang('!Log', 'Cannot close the slideshow: CopyFilePath was used less than ' .. TimeThreshold .. ' seconds ago.', 'Warning')
    end
end


-- Function to escape special characters in text for Bang commands
function escapeBangText(text)
    if text == nil then return "" end
    -- Only escape the quotes as they're the main issue with Bang commands
    local escaped = text:gsub('"', '`')
    return escaped
end

-- Function to update both sentence and metadata displays
function updateDisplay(text, metadata)
    -- Escape both text and metadata
    local safeText = escapeBangText(text)
    local safeMetadata = escapeBangText(metadata)
    
    -- Update the meters with escaped text
    SKIN:Bang('!SetOption', 'MeterQuote', 'Text', safeText)
    SKIN:Bang('!SetOption', 'MeterMETA', 'Text', safeMetadata)
    SKIN:Bang('!UpdateMeter', 'MeterQuote')
    SKIN:Bang('!UpdateMeter', 'MeterMETA')
    SKIN:Bang('!Redraw')
end

function Update()
    currentIndex = currentIndex + 1
    if currentIndex > #quoteTable then
        currentIndex = 1
    end
    currentQuoteIndex = indexList[currentIndex]
    
    local text, metadata = break_up_text(quoteTable[currentQuoteIndex])
    updateDisplay(text, metadata)
    return text
end

-- Function to navigate to the previous quote
function PreviousQuote()
    currentIndex = currentIndex - 2
    if currentIndex < 0 then
        currentIndex = #quoteTable - 1
    end
    currentQuoteIndex = indexList[currentIndex]
    
    local text, metadata = break_up_text(quoteTable[currentQuoteIndex])
    updateDisplay(text, metadata)
    return text
end

-- Function to navigate to the next quote
function NextQuote()
    if currentIndex > #quoteTable then
        currentIndex = 1
    end
    currentQuoteIndex = indexList[currentIndex]
    
    local text, metadata = break_up_text(quoteTable[currentQuoteIndex])
    updateDisplay(text, metadata)
    return text
end

-- Function to generate a unique filename based on removed line
function generateUniqueFilename(removedLine)
    local timestamp = os.time()
    local baseName = string.gsub(removedLine, "[^a-zA-Z0-9]", "_")
    return baseName .. timestamp .. ".txt"
end

-- Function to remove a specific line from a file and write it to a new file
function removeLineFromFile(filepath, lineIndex)
    local removedLine = nil
    local deleted_files_path = SKIN:GetVariable('DeletedFilesFolder')
    removedLine = quoteTable[lineIndex]
    if lineIndex >= 1 and lineIndex <= #quoteTable then
        table.remove(quoteTable, lineIndex)
    end

    local file = io.open(SKIN:MakePathAbsolute(filepath), "w")
    for _, line in ipairs(quoteTable) do
        file:write(line .. "\n\n")
    end
    file:close()

    if removedLine then
        local newFilename = generateUniqueFilename(removedLine)
        local newFilepath = deleted_files_path .. newFilename
        SKIN:Bang('!Log', 'New file created: ' .. newFilepath)
        local file = io.open(newFilepath, "w")
        file:write(removedLine .. "\n")
        file:close()
        return newFilepath
    else
        return nil
    end
end

-- Function to remove a line and re-initialize
function Remove_Line()
    local filepath = SKIN:GetVariable('TextPreset')
    local newFilepath = removeLineFromFile(filepath, tonumber(currentQuoteIndex))

    table.remove(quoteTable, currentQuoteIndex)
    Initialize()
    if newFilepath then
        SKIN:Bang('!Log', 'New file created: ' .. newFilepath)
    else
        SKIN:Bang('!Log', 'Line index out of range.')
    end
end

-- Function to open the folder containing the file
function OpenFolder()
    local filePath = SKIN:GetVariable('TextPreset')
    local folder_path = filePath:match("^(.*\\)[^\\]+$")
    local escapedPath = folder_path:gsub("\\", "\\\\")
    os.execute('start "" "' .. escapedPath .. '"')
end



-- Function to clean up the sentence by extracting the text and removing everything else
function extractSentenceAndMetadata(text)
    -- Match the sentence and metadata portions
    local sentence = text:match('"""(.-)"""')
    local metadata = text:match('""".-""","""(.-)"""')
    
    -- Return both parts, or empty strings if not found
    return sentence or "", metadata or ""
end

-- Function to process regular sentences or formatted text sentences
function break_up_text(text)
    local MAX_CHARACTERS = tonumber(SKIN:GetVariable('MAX_CHARACTERS'))
    
    -- Extract both sentence and metadata
    local extractedSentence, metadata = extractSentenceAndMetadata(text)
    
    -- If no sentence was extracted, return empty strings
    if extractedSentence == "" then
        return "", ""
    end
    
    -- Split the sentence into words
    local words = {}
    for word in extractedSentence:gmatch("%S+") do
        table.insert(words, word)
    end
    
    local lines = {}
    local currentLine = ""
    
    -- Process each word and add it to the current line
    for _, word in ipairs(words) do
        local testLine = currentLine == "" and word or currentLine .. " " .. word
        if #testLine > MAX_CHARACTERS then
            table.insert(lines, currentLine)
            currentLine = word
        else
            currentLine = testLine
        end
    end
    
    -- Add the last line if there's any remaining text
    if currentLine ~= "" then
        table.insert(lines, currentLine)
    end
    
    -- Return both the formatted text and metadata
    return table.concat(lines, "\n"), metadata
end
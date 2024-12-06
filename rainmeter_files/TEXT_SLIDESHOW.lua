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

-- Function to update the current quote index and apply text breaking
function Update()
    currentIndex = currentIndex + 1
    if currentIndex > #quoteTable then
        currentIndex = 1
    end
    currentQuoteIndex = indexList[currentIndex]
    
    local text = break_up_text(quoteTable[currentQuoteIndex])
    
    return text
end

-- Function to navigate to the previous quote
function PreviousQuote()
    currentIndex = currentIndex - 2
    if currentIndex < 0 then
        currentIndex = #quoteTable - 1
    end
    currentQuoteIndex = indexList[currentIndex]
    
    local text = break_up_text(quoteTable[currentQuoteIndex])
    
    return text
end

-- Function to navigate to the next quote
function NextQuote()
    if currentIndex > #quoteTable then
        currentIndex = 1
    end
    currentQuoteIndex = indexList[currentIndex]
    
    local text = break_up_text(quoteTable[currentQuoteIndex])
    
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



-- Function to break up text into lines that fit within specified dimensions
function break_up_text(text)
    local MAX_CHARACTERS =  tonumber(SKIN:GetVariable('MAX_CHARACTERS'))  -- Default maximum characters per line
    
    -- Split text into sentences based on punctuation marks
    local sentences = {}
    for sentence in text:gmatch("[^%.%!%?]+") do
        table.insert(sentences, sentence)
    end
    
    local lines = {}
    local currentLine = ""
    
    for _, sentence in ipairs(sentences) do
        local words = {}
        for word in sentence:gmatch("%S+") do
            table.insert(words, word)
        end
        
        for _, word in ipairs(words) do
            local testLine = currentLine == "" and word or currentLine .. " " .. word
            if #testLine > MAX_CHARACTERS then
                table.insert(lines, currentLine)
                currentLine = word
            else
                currentLine = testLine
            end
        end
        
        if currentLine ~= "" then
            table.insert(lines, currentLine)
            currentLine = ""
        end
    end
    
    return table.concat(lines, "\n")
end

def create_markdown_table(headers, columns, numRows):
    """
    Create a table in Markdown

    Args:
        headers (list | ndarray (m,)) : List of table headers
        columns (list | ndarray(m,))  : Table column data
        numRows (number)              : Number of table rows e.g. length of each column
    Returns:
        table   (str)                 : Markdown table string
    """
    table = ""

    # Create headers row and separate column headers by "|"
    # then create the next line which separates the headers
    # from the table data
    headerRow = "| "
    headerRowSep = "|"
    for header in headers:
        headerRow += header + " | "
        headerRowSep += "-" * (len(header)+2) + "|"
    
    # Construct rows
    rows = ""
    spacer = (len(headerRow)-3) // len(headers)
    headerIdx = 0
    for i in range(numRows):
        for column in columns:
            headerIdx %= len(headers)
            rows += "| " + str(column[i]) + " " * (len(headers[headerIdx]) - len(str(column[i])) + 1)
            if (headerIdx is len(headers)-1):
                rows += "|\n"
            headerIdx += 1

    return f"{headerRow}\n{headerRowSep}\n{rows}"
# AIrchive

**AIrchive** is a background tool that analyzes files in a directory and generates an AI-powered overview. It provides brief descriptions of each file and directory, along with keywords and organization suggestions. AIrchive will not modify files but will generate JSON summaries that other applications, such as **homehelp**, can use for enhanced file management.  

## Features  

- **File Analysis**: Uses Google Gemini’s API to analyze text-based files, generating meta descriptions (e.g., "this file is a list of movies") and relevant keywords.  
- **Directory Summaries**: Creates a high-level overview of a directory based on the files it contains.  
- **Organization Suggestions**: Provides recommendations for better structuring a directory without making changes itself.  
- **Background Processing**: Runs continuously on a file storage server, only working when no other jobs are running.  
- **JSON Output**: Stores AI-generated insights in JSON files that can be read by other applications.  

## Integration with homehelp  

- AIrchive will produce JSON files containing AI-generated summaries of directories.  
- homehelp will have an option to check for these files and display the AI-generated descriptions in its web interface.  

## Status  

AIrchive is currently in the **planning phase**, with development starting as a **CLI tool**. Future enhancements may include image analysis and expanded AI capabilities.  

### A disclaimer

It is probably worth noting that this is just going to be a GPT wrapper.
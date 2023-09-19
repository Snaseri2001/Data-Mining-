# Automatic SOP writing
In this project, we want to write a SOP for the field and university of the user's choice with the help of the user's input and the information we extract from the university's datasets.<br>
In this program, we first ask the user for the desired university and the field he plans to apply for. Then we get a number of desired keywords from him. These keywords are the user's personal information such as GPA, major, university where he studies, etc.
Then, according to the entered university name and field, we search in the dataset and add some related keywords to the total keywords.<br>
In the next step, we give these keywords to www.gomoonbeam.com, which is a writing assistant, to generate the motivation letter for us.<br>

## First Phase : Crawling
In this phase we have to crawl the considerable website using Selenium or beautiful soap.

## Secind Phase : Preprocessing 
In this phase we have to implement Text Preprocessing & keyword extraction, Text cleaning, Stop word removal, Tokenization etc.<br>
Next, Have a column called "extracted_keywords" and put the keywords you extracted for each string in it. Then draw the word cloud of this column.<br>
After pre-processing, a code should be written that, by taking the name of the university and the desired field, will return a number of words related to that field to the user.

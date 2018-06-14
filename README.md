# Python-scripts-answers
## Questions:
### Question 1: Please write a Python script that:

1. Reads the JSON located at http://mysafeinfo.com/api/data?list=englishmonarchs&format=json

2. Outputs a JSON object consisting of lists of unique 'nm', grouped by 'cty' and 'hse'

Example output:

{
"cty1": {
"hse1": [
"name1", 
"name2"
],
"hse2": [
"name1", 
"name2" 
] 
},
"cty2": {
"hse3": [
"name1", 
"name2"
],
"hse4": [
"name1", 
"name2" 
] 
} 
}

**Answer**: Is in file answer1.py

### Question 2: Please write a Python script that:

1. Reads the JSON located at https://data.cityofnewyork.us/api/views/25th-nujf/rows.json
2. Maps the 'name' from each field in "columns", available at JSON_ROOT['meta']['view']['columns'], to each list inside JSON_ROOT['data']. (e.g. the name of the first field listed in "columns" is the name of the first item in each list in "data")
3. Outputs a JSON file containing only data for the following fields: ["Child's First Name", "Gender", "Ethnicity", "Year of Birth", "Rank", "Count"]
4. Filters the aforementioned data to only the years 2012-2014, then groups by "Child's First Name" and "Ethnicity", and finally provides the sum of "Count" for each combination.
5. Writes the resulting data to both JSON and CSV.
6. DO NOT use the 'pandas' library when answering this question.

**Answer**: Is in answer2.py




## Contents

The following mappers and reducers work on the given file *purchases.txt*

- Give a sales breakdown by product category across all the stores with [sales_per_category](https://github.com/nancyirisarri/udacity_hadoop/tree/master/project/sales_per_category).

- Find the monetary value for the highest individual sale for each separate store with [highest_sale](https://github.com/nancyirisarri/udacity_hadoop/tree/master/project/highest_sale).

- Give the total number of sales and the total sales value from all the stores using [total_sales](https://github.com/nancyirisarri/udacity_hadoop/tree/master/project/total_sales).

The following mappers and reducers work on the given file *access_log*

- Find the number of hits on the page */assets/js/the-associates.js* with [hits_to_page](https://github.com/nancyirisarri/udacity_hadoop/tree/master/project/hits_to_page).

- How many hits were made by a specific IP address using [hits_from_ip](https://github.com/nancyirisarri/udacity_hadoop/tree/master/project/hits_from_ip).

- Find the hits and the path of the most popular file, i.e. path that occurs most often in a server access log with [most_popular](https://github.com/nancyirisarri/udacity_hadoop/tree/master/project/most_popular).

## How to Run the Files on a Cloudera Distribution including Apache Hadoop 

1.	Modify the given mapper.py and reducer.py for the input and output data.

2.	To run a test, make a subset of the data containing the first 50 lines

```shell
> head -50 data/purchases.txt > testfile
```

and simulate the pipeline

```shell
> cat testfile | code/mapper.py | sort | code/reducer.py
```

3.	Make a directory for the input and upload the dataset from the local disk to HDFS

```shell
> hadoop fs -mkdir input
> hadoop fs -put data/purchases.txt input/
```

4.	Run the job

```shell
> hs code/mapper.py code/reducer.py input output
```

5. Once the job is finished, check the output file

```shell
> hadoop fs -cat output/part-00000 | less
```
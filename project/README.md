## Contents

The following mappers and reducers work on the given file *purchases.txt*

- Give a sales breakdown by product category across all the stores, [lesson6_part2](https://github.com/nancyirisarri/udacity_hadoop/tree/master/project/lesson6_part2_salesPerCategory).

- Find the monetary value for the highest individual sale for each separate store, [lesson6_part3](https://github.com/nancyirisarri/udacity_hadoop/tree/master/project/lesson6_part3_highestSale).

- Give the total number of sales and the total sales value from all the stores, [lesson6_part4](https://github.com/nancyirisarri/udacity_hadoop/tree/master/project/lesson6_part4_totalSales).

- Find the mean of the purchases made on Sunday, [lesson7_part9](https://github.com/nancyirisarri/udacity_hadoop/tree/master/project/lesson7_part9_findingMean).

The following mappers and reducers work on the given file *access_log*

- Find the number of hits on the page */assets/js/the-associates.js*, [lesson6_part6](https://github.com/nancyirisarri/udacity_hadoop/tree/master/project/lesson6_part6_hitsToPage).

- How many hits were made by a specific IP address using [lesson6_part7](https://github.com/nancyirisarri/udacity_hadoop/tree/master/project/lesson6_part7_hitsFromIp).

- Find the hits and the path of the most popular file, i.e. path that occurs most often in a server access log with [lesson6_part8](https://github.com/nancyirisarri/udacity_hadoop/tree/master/project/lesson6_part8_mostPopular).

The following mappers and reducers work on the given file *forum_node.tsv*
- Count the uses of the word *fantastic* and find the nodes that use the word *fantastically*, [lesson7_part7](https://github.com/nancyirisarri/udacity_hadoop/tree/master/project/lesson7_part7_invertedIndex).

## How to Run the Files on a Cloudera Distribution including Apache Hadoop 

1.	Modify the given mapper.py and reducer.py for the input and output data and put in directory *code*.

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

where `hs` is an alias in the Cloudera virtual machine for 

```shell
> hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.1.jar -mapper code/mapper.py -reducer code/reducer.py -file code/mapper.py -file code/reducer.py -input input -output output
```

5. Once the job is finished, check the output file

```shell
> hadoop fs -cat output/part-00000 | less
```
## Contents

- To give a sales breakdown by product category across all the stores, use the mapper and reducer in [sales_per_category](https://github.com/nancyirisarri/udacity_hadoop/tree/master/project/sales_per_category).

- To give the monetary value for the highest individual sale for each separate store, use the files in [highest_sale](https://github.com/nancyirisarri/udacity_hadoop/tree/master/project/highest_sale).

- To give the total number of sales and the total sales value from all the stores, use the files in [total_sales](https://github.com/nancyirisarri/udacity_hadoop/tree/master/project/total_sales).

## How To
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

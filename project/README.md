## Contents

- To give a sales breakdown by product category across all the stores:
  - sales_per_category/mapper.py
  - sales_per_category/reducer.py
-

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
> hs mapper.py reducer.py input output
```

5. Once the job is finished, check the output file

```shell
> hadoop fs -cat output/part-00000 | less
```

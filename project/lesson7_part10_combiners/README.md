Contains the usual mapper in *mapper.py* and a combiner plus reducer in *reducer.py*.

Can be run with the following, where *input* contains the data and *output* will contain the result in the HDFS:

```shell
> hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.1.jar -mapper mapper.py -reducer reducer.py -combiner reducer.py -file mapper.py -file reducer.py -input input -output output
```

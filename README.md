# Apache Drill dialect for SQLAlchemy.
---
The primary purpose of this is to have a working dialect for Apache Drill that can be used with Superset 

https://github.com/airbnb/superset

Obviously, a working, robust dialect for Drill serves other purposes as well, but most of the iterative planning for this REPO will be based on working with Superset. 

Other changes will gladly be incorporated, as long as it doesn't hurt Superset integration. 

## Current Status/Development Approach
Currently we can:
- Connect to Drill
  - You need to specify schema in your connection string because superset lists tables and will error if you don't have a default schema identified.
  - SSL and Authentication is the method tested, we need to do more testing on non authenticated connections as well as non-ssl connections
- Add Tables in Superset
  - It is recommended at this time to use views. First views respond properly to describe table and you can also specify types in your views. 
- Issue queries for basic visualizations and get results. 
  - We are learning what works and what doesn't. Please make issues. 

So, we are "limping along" and working as is, but contribution and just testing/use to identify issues would be very welcome! 


## Many thanks
We need to outline that drillpy and pydrill projects both provided insight into using the restapi inthis way.

## Connection String Example:

```drill+sadrill://username:password@drillhost:drillport/dfs/yourdb?use_ssl=True```


### Install

Simply install superset via presribed methods, then on the same host, docker container, or virtual environment:

```git clone https://github.com/JohnOmernik/sadrill
cd sadrill
python3 setup.py install
cd ..```

Now you should be able to use the sadrill package with superset!




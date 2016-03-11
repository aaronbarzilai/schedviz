# schedviz
Repository for schedviz.com an open source visualizer of major sports league schedules

## Initial Project Goal
Automatically generate NBA schedule visualizations by Aaron Barzilai with help from Alejando Altaras. 

Sample:

![Sample NBA Schedule Visualization](http://schedviz.com/sample.png)

You can also view [the sample at schedviz.com](http://schedviz.com/sample.png)

## Subsequent Goals

1. Build a broader website that includes stats like record against top 4 seeds in each conference, against playoff teams, and against lottery teams as well as games remaining against each group as well as tools to share images
2. Expand to other sports, customizing the specifics as appropriate
3. Other suggestions
 
## System Design

1. schedviz.com has already been purchased by Aaron Barzilai and a sample image is at http://schedviz.com/nba/GSW.png reflecting the proposed directory structure
2. Code will be implemented in python and executed on Amazon Web Services using [AWS Lambda](https://aws.amazon.com/lambda/). Initial testing of AWS Lambda has been completed by Aaron Barzilai
3.  Based on AWS Lambda requirements, the code will be implemented in python 2.7 and utilize matplotlib, pandas, requests, and BeautifulSoup with lxml packages as needed
4.  Proposed Pseudocode executed on AWS Lambda periodically (e.g. every 5 min):
  1.  Scrape NBA.com for latest data (this will enable "real-time" updating as games complete each night)
    * Likely to involve requests, BeautifulSoup, and perhaps pandas  
  2.  Create the images for each team
    * Likely to involve matplotlib  
  3.  Update webpages with stats for each team 
    * Likely to use jinja2 templating or static website generator like hugo or Pelican
5. The website itself will be served as a static site using Amazon S3

## Notes

> I had hoped to have fleshed out more of the framework prior to the Sloan conference but haven't had a chance yet.  I would welcome your help on any aspects of the project and will work to flesh out more details of how the different functions/modules will interact. For now, I've posted the project to get it out there and solicit contributors. I'll be responsible for any costs to host and execute the site and it will always be ad-free.  By using AWS Lambda I am expecting the costs to be minimial. 
> 
> I do hope that you'll think about contributing to schedviz.com, I would welcome any assistance on both the programming and the website design.  If you're interested, please let me know.  I am at the Sloan Conference this weekend and you can reach me on twitter as [@aaronbarzilai](https://twitter.com/basketballvalue) - Aaron Barzilai 2016-03-11 02:00

# E4sy Pe4sy

## Description

Hack admin user!

## Solution

First we open that web page

![enter image description here](./figure_1.png)

Click on **Menu** (**≡**), then choose **Login**

![sdf](./figure_2.png)

Now, try **Sql Injection**

Let's give the input, like below

username = `' or ''='`

password = `' or ''='`

<img title="" src="./figure_3.png" alt="">

Then the profile page show up

<img title="" src="./figure_4.png" alt="">

We got flag!

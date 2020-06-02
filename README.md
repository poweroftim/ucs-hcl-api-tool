# UCS HCL API Tool
### Table of Contents
You're sections headers will be used to reference location of destination.

- [Description](#description)
- [How To Use](#how-to-use)
- [References](#references)

---

## Description
If you have a few different B200 blades in your UCS environment, validating hardware against the UCS HCL site can be a hassle. 

Instead, this script will do it for you. The high-level steps are...

1. Login, query your UCSM environment (blades only for now).
2. Confirm desired VMware ESXi version (you supply the version).
3. Validate blade hardware against the UCS HCL. 

---

## How To Use

#### Installation

First, go ahead and clone the repository.

`$ git clone git@github.com:poweroftim/ucs-hcl-api-tool.git`

<br>
<br>

Next, create a virtual environment to work in. Here's an example using Python3.8 on a Mac. If you're not sure where your Python version is located, use 'which'.
```
$ which python3.8
/Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8
```
<br>
<br>

Now that you know where you Python install is located, create the virtual environment. In this example, my virtual environment is 'demo3.8'
```
$ virtualenv -p /Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8 demo3.8

-output-
Running virtualenv with interpreter /Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8
Already using interpreter /Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8
Using base prefix '/Library/Frameworks/Python.framework/Versions/3.8'
New python executable in /Users/timpowe/DEMODIR/demo3.8/bin/python3.8
Also creating executable in /Users/timpowe/DEMODIR/demo3.8/bin/python
Installing setuptools, pip, wheel...
done.
```

<br>
<br>

Start the virtual environment. 
```
$ source demo3.8/bin/activate

-output-
(demo3.8)$ 
```

<br>
<br>

Navigate to the ucs-hcl-api-tool directory.
```
(demo3.8)$ cd /ucs-hcl-api-tool
```

<br>
<br>

Install the required using the requirements.txt file. 
```
(demo3.8)$ pip install -r requirements.txt

-output truncated-
Installing collected packages: args, clint, six, python-dateutil, numpy, pytz, pandas, chardet, certifi, idna, urllib3, requests, tqdm, pyparsing, ucsmsdk, requests-cache
Successfully installed args-0.1.0 certifi-2020.4.5.1 chardet-3.0.4 clint-0.5.1 idna-2.9 numpy-1.18.4 pandas-1.0.4 pyparsing-2.4.7 python-dateutil-2.8.1 pytz-2020.1 requests-2.23.0 requests-cache-0.5.2 six-1.15.0 tqdm-4.46.0 ucsmsdk-0.9.10 urllib3-1.25.9

```

<br>
<br>

Now you're ready to run the script. 
```
(demo3.8)$ python Cisco_UCS_HCL_API_Tool.py
```

<br>
<br>


If everything works, you should be greeted with the login screen. 
![Login Screen](/images/login.png)


#### API Reference

```html
    <p>coming soon!</p>
```
[Back To The Top](#read-me-template)

---

## References
[Back To The Top](#read-me-template)

```html
    <p>coming soon!</p>
```

---

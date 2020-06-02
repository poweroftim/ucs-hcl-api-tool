# UCS HCL API Tool
### Table of Contents
- [Description](#description)
- [How To Use](#how-to-use)
- [References](#references)

---

## Description
If you have a few different B200 blades in your UCS environment, validating hardware against the UCS HCL site can be a hassle. 

Instead, this script will do it for you. The high-level steps are...

1. Login and query the UCSM environment (blades only for now).
2. Identify the script which VMware ESXi version you want to install on the blades.
3. Identify which firmware version you want to upgrade to. 

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

<br>
<br>

Login to the UCSM domain using local authentication. In this example, I'm using the UCS Sandbox on DevNet (ucspe/ucspe)
![Login Screen](/images/login2.png)

<br>
<br>

Once you're logged in, the script will query each of your blades along with each blade's processor and adapter versions. 
![Login Screen](/images/query.png)

<br>
<br>

Next, you'll enter the VMware ESXi version you want to run on the blades. You can come back to this later if you need to.
![Login Screen](/images/vmwareversion.png)

<br>
<br>

Then, you'll enter the blade firmware version you want to run. This list is dependent on the VMware ESXi version. If you don't see the version you want on the list, you'll may need to enter a different ESXi version. If the firmeware version you're looking for still isn't available, your blades may not support that firmware version. Check with the release notes for that version to confirm. 
![Login Screen](/images/firmwareversion.png)





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

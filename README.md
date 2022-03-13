# Simple shapeshifter malware in Python!

**This project  is subject to change!**

I made this project to test my Python skills, i have no responsibility for the use of this program.

Bellow have a fluxgram of malware ideia:
```mermaid
graph LR
A(Program no infected) --> B(Download the malware)
B --> C(Execute Malware)
C --> D(Malware clone legit program to choosed dir)
D --> E(Malware rename yourself name to legit program)
E --> F(On execute the 'legit' infected program)
F --> G(Run the legit program cloned)
F --> H(Run malware script)
```

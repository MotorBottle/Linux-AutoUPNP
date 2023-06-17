# Linux-AutoUPNP
Auto UPNP mapping script so that you can mantain the ports (when you are not admin of the router).

To run the script every 3 mins, you can run the following code in terminal:

crontab -e

*/3 * * * * python3 <PATH TO YOU FILE>/autoupnp.py

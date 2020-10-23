# JasminHTTPBridge

This is meant to be a bridge that takes advantage of [Jasmin](https://github.com/jookies/jasmin)'s Interceptor. It probably isn't the most efficient way to do almost anything, but it is the most extensible and will likely often be the easiest.

This does not currently support delivery receipts, but that is an important goal currently.

## How to Use

First, because of how Jasmin works, you will need to edit the variable bridge.py BRIDGE_PATH to be the correct path to the directory with your script and config.

Create a file called conf.json after creating this directory. It should be a JSON array, and for each endpoint it should have an element that looks like this:

```json
{
    "url": "your url here",
    "method": "GET or POST"
}
```

Then, make sure the Jasmin interceptor daemon is running and add your MT interceptor in jcli:

```
jcli : mtinterceptor -a
> type DefaultInterceptor
> script python2(<PATH TO SCRIPT>)
> ok
```

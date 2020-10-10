# JasminHTTPBridge

This is meant to be a bridge that takes advantage of [Jasmin](https://github.com/jookies/jasmin)'s Interceptor. It probably isn't the most efficient way to do almost anything, but it is the most extensible and will likely often be the easiest.

This does not currently support delivery receipts, but that is an important goal currently.

## How to Use

Create a file called conf.json after creating this directory. Fill in the following values:

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

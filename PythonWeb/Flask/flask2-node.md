# Flask 2

- Variable Rules

>You can add variable sections to a URL by marking sections with &lt;variable_name&gt;. Your function then receives the &lt;variable_name&gt; as a keyword argument. Optionally, you can use a converter to specify the type of the argument like &lt;converter:variable_name&gt;.

| Type | Value|
| --- | --- |
|string|(default) accepts any text without a slash|
|int|accepts positive integers|
|float|accepts positive floating point values|
|path|like string but also accepts slashes|
|uuid|accepts UUID strings|

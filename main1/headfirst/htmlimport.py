import html

escaped_html = html.escape("This fragment contains <script>script</script> tag")
print(escaped_html)
unescaped_html = html.unescape(escaped_html)
print(unescaped_html)
# _*_ coding=utf-8 _*_


from lxml import etree

text = """
<div>
    <ul>
        <li class="item-0"><a href="link1.html">first item</a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-active"><a href="link3.html">third item</a></li>
        <li class="item-4"><a href="link4.html">fourth item</a></li>
        <li class="item-5"><a href="link5.html">fifth item</a>
    </ul>
</div>
"""
html = etree.HTML(text)
res = etree.tostring(html)
print(res.decode('utf-8'))


# html = etree.parse('./text.html', etree.HTMLParser())
# print(etree.tostring(html).decode('utf-8'))

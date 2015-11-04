
{% capture this_year %}{{site.time | date:"%Y"}}{% endcapture %}
{% for year in (2009..{{this_year}}) reversed %}

### {{ year }}
{% bibliography --query @*[year={{ year }}] %}

{% endfor %}

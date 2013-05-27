vim:
  package:
    {% if   grains['os_family'] == 'RedHat' %}
    name: vim-enhanced
    {% elif grains['os_family'] == 'Debian' %}
    name: vim
    {% endif %}
  
  conf: 
    vimrc: salt://edit/vimrc

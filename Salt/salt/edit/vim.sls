vim:
  pkg:
    - installed
    - name: {{ pillar['vim']['package']['name'] }}

/etc/vimrc:
  file.managed:
    - source: {{ pillar['vim']['conf']['vimrc'] }}
    - mode: 644
    - user: root
    - group: root
    - require:
      - pkg: vim

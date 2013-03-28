""文件名:  .vimrc
""日期:    Thu 28 Mar 2013 06:00:24 PM CST
""作者:    Shanjie Luo, Dong Guo


""快捷键
""==================================================================
" Ctrl + H                   --光标移行首
" Ctrl + J                   --光标移下一行行首
" Ctrl + K                   --光标移上一行行尾
" Ctrl + L                   --光标移行尾
" Ctrl + Z                   --取代ESC模式键 [和部分软件的快捷键有冲突]
" Ctrl + S                   --保存文件
" Ctrl + C                   --编译 [支持C/C++、Java、Haskell]
" Ctrl + R                   --运行 [支持C/C++、Java、Haskell、Lua、Perl、Python、Ruby]
" Ctrl + ]                   --转到函数定义
" Ctrl + T                   --返回调用函数
" Ctrl + E                   --添加注释 [插入模式，添加的是C语言的多行注释，所以适用于C/C++/Java等]
" <C-P>                      --单词补全
" <C-X><C-L>                 --整行补全
" Tab键                      --插入模式下的全功能语法结构补全 [pydiction插件]
" Shift + Insert             --向Vim中粘贴从别处复制的内容
" za                         --打开或关闭当前折叠
" zM                         --关闭所有折叠
" zR                         --打开所有折叠
" :set syntax=cpp            --手动选择语法高亮 [或 :set filetype=cpp]
" :%!xxd                     --转储二进制文件，以十六进制形式显示
" :%!xxd -r                  --还原二进制文件


""配置选项
""==================================================================
colorscheme inkpot           " 着色模式

set history=400              " 记住历史的操作命令，默认是20
set term=xterm-color         " 指定终端
set guifont=Monaco:h10       " 字体 && 字号
set tabstop=4                " 设置tab键的宽度
set shiftwidth=4             " 换行时行间交错使用4个空格
set autoindent               " 自动对齐
set backspace=2              " 设置退格键可用
set cindent shiftwidth=4     " 自动缩进4空格
set smartindent              " 智能自动缩进
set ai                       " 设置自动缩进
set nu                       " 显示行号
set showmatch                " 显示括号配对情况
"set mouse=a                 " 启用鼠标
"set ruler                   " 右下角显示光标位置的状态行
"set incsearch               " 查找book时，当输入/b时会自动找到，开启实时搜索功能
set hlsearch                 " 开启高亮显示结果
set nowrapscan               " 搜索到文件两端时不重新搜索
"set nocompatible            " 关闭兼容模式
set vb t_vb=                 " 关闭提示音
set cursorline               " 突出显示当前行
set hidden                   " 允许在有未保存的修改时切换缓冲区

set list                     " 显示Tab符，使用一高亮竖线代替
set listchars=tab:\|\ ,
set expandtab

syntax enable                " 打开语法高亮
syntax on                    " 开启文件类型侦测
filetype indent on           " 针对不同的文件类型采用不同的缩进格式
filetype plugin on           " 针对不同的文件类型加载对应的插件
filetype plugin indent on    " 启用自动补全

"设置backspace
set backspace=indent,eol,start

"每行超过80个的字符用下划线标示
au BufRead,BufNewFile *.asm,*.c,*.cpp,*.java,*.cs,*.sh,*.lua,*.pl,*.pm,*.py,*.rb,*.erb,*.hs,*.vim 2match Underlined /.\%81v/

"状态栏显示
set statusline=%F%m\ %r,%Y,%{&fileformat}\ \ \ ASCII=\%b,HEX=\%B\ \ \ Row=%l,Column=%c%V\ %p%%\ \ \ [\ %L\ lines\ in\ all\ ] 

"设置编码
set fenc=utf-8
set encoding=utf-8
set fileencodings=utf-8,gbk,cp936,latin-1

"解决consle输出乱码
language messages zh_CN.utf-8

"TxtBrowser 高亮TXT文本文件
au BufRead,BufNewFile *.txt setlocal ft=txt

""插件配置
""==================================================================
"Taglist
let Tlist_Ctags_Cmd='/usr/bin/ctags'
let Tlist_Show_One_File=1                    " 只显示当前文件的tags
let Tlist_Exit_OnlyWindow=1                  " 如果Taglist窗口是最后一个窗口则退出Vim
let Tlist_Use_Right_Window=1                 " 在右侧窗口中显示
let Tlist_File_Fold_Auto_Close=1             " 自动折叠
nnoremap <silent> <F12> :Tlist<CR>
nnoremap <silent> <F11> :TlistSync<CR>
nnoremap <silent> <F9> <C-W>w

"FencView 查看和更改文件编码
let g:fencview_autodetect=1

"Minibufexpl 多文件编辑
let g:miniBufExplMapWindowNavVim = 1
let g:miniBufExplMapWindowNavArrows = 1   
let g:miniBufExplMapCTabSwitchBufs = 1   
let g:miniBufExplModSelTarget = 1 

"pydiction Python自动补全
filetype plugin on
let g:pydiction_location = '~/.vim/tools/pydiction/complete-dict'


""引号、括号自动匹配 
""==================================================================
:inoremap ( ()<ESC>i
:inoremap ) <c-r>=ClosePair(')')<CR>

:inoremap { {}<ESC>i
:inoremap } <c-r>=ClosePair('}')<CR>

:inoremap [ []<ESC>i
:inoremap ] <c-r>=ClosePair(']')<CR>

":inoremap < <><ESC>i
":inoremap > <c-r>=ClosePair('>')<CR>

:inoremap " ""<ESC>i
:inoremap ' ''<ESC>i

:inoremap ` ``<ESC>i

function ClosePair(char)
    if getline('.')[col('.') - 1] == a:char
        return "\<Right>"
    else
        return a:char
    endif
endf


""自定义函数
""==================================================================
"加载语法模板和作者、时间信息 [非插入模式]
function Mytitle()
    call append(0, "#!/usr/bin/env python")
    call append(1, "#-*- coding:utf-8 -*-")
    call append(2, "")
    call append(3, "# FileName: ".expand("%"))
    call append(4, "# Date: ".strftime("%c"))
    call append(5, "# Author: Dong Guo")
endf

function Myclass() 
    call append(line("."), "/// @class:\t")
    call append(line(".")+1, "/// @brief:\t")
endf

"映射到快捷键
map <F2> <Esc>:call Mytitle()<CR><Esc>
map <F3> <Esc>:call Myclass()<CR><Esc>



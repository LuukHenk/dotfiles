" Load plugins
call plug#begin('~/.vim/plugged')
Plug 'chriskempson/base16-vim'				" Base 16 colorset
Plug 'itchyny/lightline.vim'					" Light cursor line
Plug 'tpope/vim-commentary'						" Easy commenting of line using 'gcc'
Plug 'tpope/vim-endwise'							" Automatically add end to certain structures
Plug 'tpope/vim-repeat'               " Use '.' to repeat last used command
Plug 'tpope/vim-surround'             " Easily change surrounding using 'cs<previous_surr><new_surr>'
Plug 'w0rp/ale'												" Syntax linting
Plug 'haya14busa/incsearch.vim'				" Use '/' to search in text
Plug 'junegunn/vim-easy-align'        " Easily allign text usng 'gaip'
Plug 'junegunn/fzf.vim'               " ?
Plug 'machakann/vim-highlightedyank'  " Highlight when yanked
Plug 'google/vim-searchindex'         " Shows how many times a searched pattern occurs
call plug#end()

" Settings

set ignorecase " Ignore case
set smartcase  " Use case when it thinks you entendidly added it
set shiftwidth=2 " Set tabsize as 2 spaces
set softtabstop=2 " Set tabsize as 2 spaces
set tabstop=2 " Set tabsize as 2 spaces
set noshowmode " Don't show insert
set cursorline " Highlight the cursor line
set nobackup " Don't make backup files
set termguicolors " Use the colors of the terminal gui
set noswapfile " Don't use swap files
"
" Colors
"
colorscheme base16-default=dark

" Map keys
imap <Up> <Nop>
imap <Down> <Nop>
imap <Left> <Nop>
imap <Right> <Nop>
nmap <Up> <Nop>
nmap <Down> <Nop>
nmap <Left> <Nop>
nmap <Right> <Nop>
nmap <S-s> <Nop>
nmap >> <Nop>
nmap << <Nop>
vmap >> <Nop>
vmap << <Nop>
map $ <Nop>
map ^ <Nop>
map { <Nop>
map } <Nop>
map <C-z> <Nop>
nmap <silent> q: :q<cr>
nmap <silent> Q: :q<cr>
inoremap <C-k> <Up>
inoremap <C-j> <Down>
inoremap <C-h> <Left>
inoremap <C-l> <Right>
noremap K {
noremap J }
noremap H ^
noremap L $

nnoremap <C-s> :write<cr>
vnoremap <C-s> <C-c>:write<cr>
inoremap <C-s> <Esc>:write<cr>
onoremap <C-s> <Esc>:write<cr>

inoremap <>   <><Left>
inoremap ()   ()<Left>
inoremap {}   {}<Left>
inoremap []   []<Left>
inoremap ""   ""<Left>
inoremap ''   ''<Left>
inoremap ``   ``<Left>

nnoremap <tab>   >>
nnoremap <S-tab> <<
vnoremap <tab>   >><Esc>gv
vnoremap <S-tab> <<<Esc>gv

" Lightline {{{
  let s:base1   = '#C8CACB'
  let s:base0   = '#AEB0B1'
  let s:base00  = '#949697'
  let s:base02  = '#626465'
  let s:base023 = '#484A4B'
  let s:base03  = '#2F3132'
  let s:red     = '#cd3f45'
  let s:orange  = '#db7b55'
  let s:yellow  = '#e6cd69'
  let s:green   = '#9fca56'
  let s:cyan    = '#55dbbe'
  let s:blue    = '#55b5db'
  let s:magenta = '#a074c4'

  let s:p                = {'normal': {}, 'inactive': {}, 'insert': {}, 'replace': {}, 'visual': {}, 'tabline': {}}
  let s:p.normal.left    = [ [ s:blue,   s:base03  ], [ s:base03, s:blue   ] ]
  let s:p.normal.middle  = [ [ s:base1,  s:base03  ]  ]
  let s:p.normal.right   = [ [ s:base03, s:blue    ], [ s:base00, s:base03 ] ]
  let s:p.normal.error   = [ [ s:red,    s:base023 ]  ]
  let s:p.normal.warning = [ [ s:yellow, s:base02  ]  ]

  let s:p.inactive.left   = [ [ s:base1,   s:base03  ], [ s:base03, s:base03  ] ]
  let s:p.inactive.middle = [ [ s:base03,  s:base03  ]  ]
  let s:p.inactive.right  = [ [ s:base03,  s:base03  ], [ s:base03, s:base03  ] ]

  let s:p.insert.left     = [ [ s:green,   s:base03  ], [ s:base03, s:green   ] ]
  let s:p.insert.right    = [ [ s:base03,  s:green   ], [ s:base00, s:base03  ] ]
  let s:p.replace.left    = [ [ s:orange,  s:base03  ], [ s:base03, s:orange  ] ]
  let s:p.replace.right   = [ [ s:base03,  s:orange  ], [ s:base00, s:base03  ] ]
  let s:p.visual.left     = [ [ s:magenta, s:base03  ], [ s:base03, s:magenta ] ]
  let s:p.visual.right    = [ [ s:base03,  s:magenta ], [ s:base00, s:base03  ] ]

	let g:lightline#colorscheme#base16_seti#palette = lightline#colorscheme#fill(s:p)
  let g:lightline = {
        \ 'colorscheme':      'base16_seti',
        \ 'separator':        { 'left': "", 'right': "" },
        \ 'subseparator':     { 'left': "│", 'right': "│" },
        \ 'active': {
        \   'left': [ [ 'mode', 'paste' ],
        \             [ 'modified', 'fugitive', 'label' ] ],
        \   'right': [ [ 'lineinfo' ],
        \              [ 'filetype' ] ]
        \ },
        \ 'component': {
        \   'mode':     '%{lightline#mode()[0]}',
        \   'readonly': '%{&filetype=="help"?"":&readonly?"!":""}',
        \   'modified': '%{&filetype=="help"?"":&modified?"+":&modifiable?"":"-"}',
        \   'fugitive': '%{exists("*fugitive#head")?fugitive#head():""}',
        \   'label':    '%{substitute(expand("%"), "NetrwTreeListing \\d\\+", "netrw", "")}'
        \ },
        \ 'component_visible_condition': {
        \   'paste':    '(&paste!="nopaste")',
        \   'readonly': '(&filetype!="help"&& &readonly)',
        \   'modified': '(&filetype!="help"&&(&modified||!&modifiable))',
        \   'fugitive': '(exists("*fugitive#head") && ""!=fugitive#head())'
        \ }
        \ }
" }}}

" Ale {{{
  let g:ale_set_highlights       = 0                            " only show errors in sign column
  let g:ale_echo_msg_error_str   = 'E'                          " error sign
  let g:ale_echo_msg_warning_str = 'W'                          " warning sign
  let g:ale_echo_msg_format      = '[%linter%] %s [%severity%]' " status line format
  let g:ale_statusline_format    = ['⨉ %d', '⚠ %d', '⬥ ok']     " error status format
  let g:ale_lint_delay           = 500                      " relint max once per [amount] milliseconds
  let g:ale_linters              = {
        \ 'ruby': ['rubocop'],
        \ 'javascript': ['eslint'],
        \ 'fish': []
        \ }
" }}}

fun! s:StripWS()
  if (&ft =~ 'vader') | return | endif
  %s/\s\+$//e
endfun
  " convenience function for setting filetype specific spacing
if !exists('*s:IndentSize')
  function! s:IndentSize(amount)
    exe "setlocal expandtab ts=" . a:amount . " sts=" . a:amount . " sw=" . a:amount
  endfunction
endif

augroup Files
  au!
  au BufWritePre *                call s:StripWS()     " remove trailing whitespace before saving buffer
  au FileType javascript,jsx,json call s:IndentSize(4) " 4 space indents for JS/JSX/JSON
  au FileType markdown,python     call s:IndentSize(4) " 4 space indents for markdown and python
augroup END

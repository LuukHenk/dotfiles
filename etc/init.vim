" Load plugins
call plug#begin('~/.vim/plugged')
Plug 'chriskempson/base16-vim'				" Base 16 colorset
Plug 'tpope/vim-commentary'						" Easy commenting of line using 'gcc'
Plug 'tpope/vim-endwise'							" Automatically add end to certain structures
Plug 'tpope/vim-repeat'               " Use '.' to repeat last used command
Plug 'tpope/vim-surround'             " Easily change surrounding using 'cs<previous_surr><new_surr>'
Plug 'w0rp/ale'												" Syntax linting
Plug 'haya14busa/incsearch.vim'				" FIXME add config
Plug 'junegunn/vim-easy-align'        " FIXME
Plug 'machakann/vim-highlightedyank'  " Highlight when yanked
Plug 'google/vim-searchindex'         " Shows how many times a searched pattern occurs
call plug#end()

" Settings

set ignorecase " Ignore case
set smartcase  " Use case when it thinks you entendidly added it
set shiftwidth=4
set softtabstop=4
set tabstop=4
set noshowmode " Don't show insert
set cursorline " Highlight the cursor line
set nobackup " Don't make backup files
set termguicolors " Use the colors of the terminal gui
set noswapfile " Don't use swap files

" Colors

colorscheme base16-default-dark " Set color sceme

" Map keys
"
" Check keymapping: :h <key>
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

" {{{ Status bar
  let g:mode_colors = {
        \ 'n':  'StatusLineSection',
        \ 'v':  'StatusLineSectionV',
        \ '': 'StatusLineSectionV',
        \ 'i':  'StatusLineSectionI',
        \ 'c':  'StatusLineSectionC',
        \ 'r':  'StatusLineSectionR'
        \ }

  fun! StatusLineRenderer()
    let hl = '%#' . get(g:mode_colors, tolower(mode()), g:mode_colors.n) . '#'

    return hl
          \ . (&modified ? ' + │' : '')
          \ . ' %{StatusLineFilename()} %#StatusLine#%='
          \ . hl
          \ . ' %l:%c '
  endfun

  fun! StatusLineFilename()
    if (&ft ==? 'netrw') | return '*' | endif
    return substitute(expand('%'), '^' . getcwd() . '/\?', '', 'i')
  endfun

  fun! <SID>StatusLineHighlights()
    hi StatusLine         ctermbg=8  guibg=#313131 ctermfg=15 guifg=#cccccc
    hi StatusLineNC       ctermbg=0  guibg=#313131 ctermfg=8  guifg=#999999
    hi StatusLineSection  ctermbg=8  guibg=#55b5db ctermfg=0  guifg=#333333
    hi StatusLineSectionV ctermbg=11 guibg=#a074c4 ctermfg=0  guifg=#000000
    hi StatusLineSectionI ctermbg=10 guibg=#9fca56 ctermfg=0  guifg=#000000
    hi StatusLineSectionC ctermbg=12 guibg=#db7b55 ctermfg=0  guifg=#000000
    hi StatusLineSectionR ctermbg=12 guibg=#ed3f45 ctermfg=0  guifg=#000000
  endfun

  call <SID>StatusLineHighlights()

  " only set default status line once on initial startup.
  " ignored on subsequent 'so $MYVIMRC' calls to prevent
  " active buffer statusline from being 'blurred'.
  if has('vim_starting')
    let &statusline = ' %{StatusLineFilename()}%= %l:%c '
  endif
" }}}

" Ale {{{
" FIXME add python and bash
  let g:ale_set_highlights       = 0                            " only show errors in sign column
  let g:ale_echo_msg_error_str   = 'E'                          " error sign
  let g:ale_echo_msg_warning_str = 'W'                          " warning sign
  let g:ale_echo_msg_format      = '[%linter%] [%severity%] %s' " status line format
  let g:ale_statusline_format    = ['⨉ %d', '⚠ %d', '⬥ ok']     " error status format
  let g:ale_lint_delay           = 500                      " relint max once per [amount] milliseconds
  let g:ale_linters              = {
        \ 'ruby': ['rubocop'],
        \ 'javascript': ['eslint'],
        \ 'fish': []
        \ }
" }}}

" convenience function for setting filetype specific spacing
function! s:IndentSize(amount)
  exe "setlocal expandtab ts=" . a:amount . " sts=" . a:amount . " sw=" . a:amount
endfunction

augroup Files
  au!
  " auto reload file changes outside of vim, toggle custom status bar,
  " and toggle cursorline for active buffer.
  au FocusGained,VimEnter,WinEnter,BufWinEnter *
    \ setlocal cursorline& statusline& |
    \ setlocal cursorline  statusline=%!StatusLineRenderer() |
    \ checktime

  " restore above settings when leaving buffer / vim
  au FocusLost,VimLeave,WinLeave,BufWinLeave *
  \ setlocal statusline& cursorline&
  au BufWritePre * %s/\s\+$//e    " remove trailing whitespace before saving buffer
  au FileType markdown,vim call s:IndentSize(2) " 2 space indents for markdown and python
augroup END



-- luacheck: globals vim

local augroup = "init.lua"
vim.api.nvim_create_augroup(augroup, {})

vim.loader.enable()

local statuslines = {
	inactive = " %{v:lua.custom_status_line_filename()}%= %l:%c ",
	active = "%!v:lua.custom_status_line()",
}

-- globals {{{
vim.g.mapleader = " "
vim.g.loaded_node_provider = 0
vim.g.loaded_ruby_provider = 0
vim.g.loaded_perl_provider = 0
vim.g.loaded_python3_provider = 0
-- }}}

-- settings {{{
local undo_directory = vim.env.HOME .. "/.local/share/nvim/undo//"
local backup_directory = vim.env.HOME .. "/.local/share/nvim/backup//"

vim.opt.list = true
vim.opt.wrap = false
vim.opt.ruler = false
vim.opt.relativenumber = true
vim.opt.tabstop = 2
vim.opt.showmode = false
vim.opt.undofile = true
vim.opt.swapfile = false
vim.opt.smartcase = true
vim.opt.expandtab = true
vim.opt.backupcopy = "yes"
vim.opt.ignorecase = true
vim.opt.cursorline = true
vim.opt.splitbelow = true
vim.opt.splitright = true
vim.opt.shiftwidth = 0
vim.opt.timeoutlen = 1000
vim.opt.updatetime = 100
vim.opt.statusline = statuslines.inactive
vim.opt.softtabstop = 2
vim.opt.showtabline = 0
vim.opt.termguicolors = true
vim.opt.path:append({ "**" })
vim.opt.undodir:prepend({ undo_directory })
vim.opt.backupdir:prepend({ backup_directory })
vim.opt.clipboard:append({ "unnamedplus" })
vim.opt.listchars:append({ nbsp = "+", tab = "‣ ", trail = "•" })
vim.opt.fillchars:append({ msgsep = " ", vert = "│", eob = " " })
vim.opt.wildignore:append({ ".git", ".DS_Store", "node_modules" })
vim.opt.completeopt:append({ "menu", "menuone", "noselect" })
vim.opt.virtualedit:append({ "onemore" })

for _, path in ipairs({ undo_directory, backup_directory }) do
	if vim.fn.isdirectory(path) == 0 then
		vim.fn.mkdir(path, "p")
	end
end
-- }}}

-- plugins {{{
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.uv.fs_stat(lazypath) then
	vim.fn.system({
		"git",
		"clone",
		"--filter=blob:none",
		"https://github.com/folke/lazy.nvim.git",
		"--branch=stable",
		lazypath,
	})
end

vim.opt.rtp:prepend(lazypath)

require("lazy").setup({
	{
		"ibhagwan/fzf-lua",
		keys = { "<C-f>", "<C-g>" },
		config = function()
			local fzf_lua = require("fzf-lua")

			fzf_lua.setup({
				actions = {
					files = {
						["default"] = fzf_lua.actions.file_edit_or_qf,
						["ctrl-x"] = fzf_lua.actions.file_split,
						["ctrl-v"] = fzf_lua.actions.file_vsplit,
					},
				},
				winopts = function()
					local height = 15

					return {
						border = { "—", "—", "—", "", "", "", "", "" },
						row = vim.o.lines - vim.o.cmdheight - 3 - height,
						column = 1,
						height = height,
						width = vim.o.columns + 1,
					}
				end,
			})

			vim.keymap.set("n", "<C-f>", function()
				fzf_lua.files({
					prompt = "> ",
					previewer = false,
					cwd_prompt = false,
					rg_opts = [[--color=never --files --hidden --follow --no-ignore -g "!.git/**" -g "!node_modules/**" -g "!.DS_Store"]],
					fzf_opts = { ["--info"] = "inline" },
				})
			end)

			vim.keymap.set("n", "<C-g>", function()
				fzf_lua.live_grep_native({
					prompt = "> ",
					no_header_i = false,
					previewer = false,
					exec_empty_query = true,
					fzf_opts = { ["--info"] = "inline", ["--nth"] = "2.." },
				})
			end)
		end,
	},

	{
		"mhartington/formatter.nvim",
		event = { "BufReadPre" },
		config = function()
			local function prettier_no_ignore(fn)
				return function(...)
					local settings = fn(...)

					if type(settings.args) ~= "table" then
						settings.args = {}
					end

					settings.args[#settings.args + 1] = "--ignore-path no-ignore"

					return settings
				end
			end

			local stylua = require("formatter.filetypes.lua").stylua
			local filetype_config = {
				lua = { stylua },
			}
			local filetype_exts = table.concat(
				vim.tbl_map(function(k)
					return string.format("*.%s", k)
				end, {
					"lua",
				}),
				","
			)

			require("formatter").setup({ filetype = filetype_config })
			vim.api.nvim_create_autocmd({ "BufWritePost" }, {
				group = augroup,
				pattern = filetype_exts,
				callback = function()
					local ok = pcall(vim.cmd.FormatWrite)

					if not ok then
						vim.api.nvim_echo({ { "Failed to format buffer!", "ErrorMsg" } }, false, {})
					end
				end,
			})
		end,
	},

	{
		"kylechui/nvim-surround",
		event = { "BufReadPre" },
		config = function()
			require("nvim-surround").setup()
		end,
	},

	{
		"RRethy/nvim-base16",
		event = { "ColorScheme" },
		config = function() end,
	},
	{
		"sidofc/carbon.nvim",
		config = function()
			require("carbon").setup({
				sync_pwd = true,
				indicators = { collapse = "▾", expand = "▸" },
				actions = { toggle_recursive = "<s-cr>" },
				file_icons = false,
				highlights = {
					CarbonExe = { link = "@string" },
				},
			})
		end,
	},
	{
		"nvim-treesitter/nvim-treesitter",
		build = ":TSUpdate",
		event = { "BufRead" },
		config = function()
			require("nvim-treesitter.configs").setup({
				indent = { enable = true },
				highlight = { enable = true },
				ensure_installed = {
					"bash",
					"html",
					"javascript",
					"json",
					"lua",
					"python",
					"rust",
					"toml",
					"tsx",
					"typescript",
				},
			})
		end,
	},
})
-- }}}

-- mappings {{{
vim.keymap.set({ "n", "v", "o" }, ">>", "<Nop>")
vim.keymap.set({ "n", "v", "o" }, "<<", "<Nop>")

vim.keymap.set("n", "$", "<Nop>")
vim.keymap.set("n", "^", "<Nop>")
vim.keymap.set("n", "{", "<Nop>")
vim.keymap.set("n", "}", "<Nop>")
vim.keymap.set({ "n", "v", "o" }, "K", "{")
vim.keymap.set({ "n", "v", "o" }, "J", "}")
vim.keymap.set({ "n", "v", "o" }, "H", "^")
vim.keymap.set({ "n", "v", "o" }, "L", "$")

vim.keymap.set({ "n" }, "<C-h>", ":wincmd h<cr>")
vim.keymap.set({ "n" }, "<C-j>", ":wincmd j<cr>")
vim.keymap.set({ "n" }, "<C-k>", ":wincmd k<cr>")
vim.keymap.set({ "n" }, "<C-l>", ":wincmd l<cr>")

vim.keymap.set("i", "<C-k>", "<Up>")
vim.keymap.set("i", "<C-j>", "<Down>")
vim.keymap.set("i", "<C-h>", "<Left>")
vim.keymap.set("i", "<C-l>", "<Right>")

vim.keymap.set("n", "<C-s>", ":write<Cr>", { silent = true })
vim.keymap.set("v", "<C-s>", "<C-c>:write<Cr>gv", { silent = true })
vim.keymap.set("i", "<C-s>", "<C-o>:write<Cr>", { silent = true })
vim.keymap.set("o", "<C-s>", "<Esc>:write<Cr>", { silent = true })

vim.keymap.set("i", "<>", "<><Left>")
vim.keymap.set("i", "()", "()<Left>")
vim.keymap.set("i", "{}", "{}<Left>")
vim.keymap.set("i", "[]", "[]<Left>")
vim.keymap.set("i", '""', '""<Left>')
vim.keymap.set("i", "''", "''<Left>")
vim.keymap.set("i", "``", "``<Left>")

vim.keymap.set("n", "<Tab>", ">>")
vim.keymap.set("n", "<S-Tab>", "<<")
vim.keymap.set("v", "<Tab>", ">><Esc>gv")
vim.keymap.set("v", "<S-Tab>", "<<<Esc>gv")
vim.keymap.set("i", "<S-Tab>", "<C-d>")

vim.keymap.set("v", "i<Bar>", ":<C-u>normal! T<Bar>vt<Bar><Cr>")
vim.keymap.set("o", "i<Bar>", ":<C-u>normal! T<Bar>vt<Bar><Cr>")
vim.keymap.set("v", "a<Bar>", ":<C-u>normal! F<Bar>vf<Bar><Cr>")
vim.keymap.set("o", "a<Bar>", ":<C-u>normal! F<Bar>vf<Bar><Cr>")

vim.keymap.set("n", "U", "<C-r>")
vim.keymap.set("n", "<C-S-x>", "<C-x>")
vim.keymap.set("n", "<C-x>", "<C-a>")

vim.keymap.set("n", "<C-n>", function()
	return pcall(vim.cmd.cnext) or pcall(vim.cmd.cfirst)
end)

vim.keymap.set("n", "<C-p>", function()
	return pcall(vim.cmd.cprev) or pcall(vim.cmd.clast)
end)

vim.keymap.set("n", "<C-w>", function()
	local winid = vim.api.nvim_get_current_win()
	local windows = vim.fn.getwininfo()

	if #windows > 1 then
		vim.api.nvim_win_close(winid, false)
	elseif vim.bo.filetype ~= "carbon.explorer" then
		pcall(vim.cmd.Carbon)
	end
end, { nowait = true })
-- }}}

-- statusline and cursorline {{{
local severity_labels = { "Error", "Warn", "Info", "Hint" }
local status_mode_groups = {
	n = "StatusLineSection",
	i = "StatusLineSectionI",
	c = "StatusLineSectionC",
	r = "StatusLineSectionR",
	v = "StatusLineSectionV",
	["\22"] = "StatusLineSectionV",
}

function _G.custom_status_line_lsp()
	local counts = { 0, 0, 0, 0 }
	local segment = ""

	for _, diagnostic in ipairs(vim.diagnostic.get(0)) do
		counts[diagnostic.severity] = counts[diagnostic.severity] + 1
	end

	for severity_index, count in ipairs(counts) do
		if count > 0 then
			local type = severity_labels[severity_index]

			segment = string.format("%s%%#StatusLineLsp%s# %d%s ", segment, type, count, type:sub(0, 1))
		end
	end

	return segment
end

function _G.custom_status_line_filename()
	local filename = vim.fn.fnamemodify(vim.api.nvim_buf_get_name(0), ":~:.")

	if vim.bo.filetype == "qf" then
		filename = "quickfix"
	elseif string.match(filename, "^term:") then
		filename = "terminal"
	elseif string.match(filename, "^~") then
		filename = vim.fn.fnamemodify(filename, ":t")
	elseif vim.b.carbon and vim.b.carbon.path then
		filename = string.gsub(vim.b.carbon.path, vim.fn.fnamemodify(vim.uv.cwd(), ":h") .. "/", "")
	end

	return filename
end

function _G.custom_status_line()
	local mode = vim.api.nvim_get_mode().mode:lower()
	local group = status_mode_groups[mode] or status_mode_groups.n

	return string.format(
		"%%#%s#%s %s %s%%#StatusLine#%%=%%#%s# %%l:%%c ",
		group,
		vim.bo.modified and " + |" or "",
		_G.custom_status_line_filename(),
		_G.custom_status_line_lsp(),
		group
	)
end
-- }}}

-- autocommands {{{
vim.api.nvim_create_autocmd({ "DiagnosticChanged" }, {
	group = augroup,
	pattern = "*",
	callback = function(data)
		if data.buf == vim.api.nvim_get_current_buf() then
			vim.wo.statusline = statuslines.active
		end
	end,
})

vim.api.nvim_create_autocmd({ "FocusLost", "VimLeave", "WinLeave", "BufLeave" }, {
	group = augroup,
	pattern = "*",
	callback = function()
		vim.wo.cursorline = false
		vim.wo.statusline = statuslines.inactive
	end,
})

vim.api.nvim_create_autocmd({ "FocusGained", "VimEnter", "WinEnter", "BufEnter" }, {
	group = augroup,
	pattern = "*",
	callback = function()
		vim.wo.cursorline = true
		vim.wo.statusline = statuslines.active
	end,
})

vim.api.nvim_create_autocmd({ "BufEnter" }, { group = augroup, pattern = "global", callback = vim.cmd.checktime })

vim.api.nvim_create_autocmd("VimResized", {
	group = augroup,
	callback = function()
		vim.cmd.wincmd("=")
	end,
})

vim.api.nvim_create_autocmd("TextYankPost", {
	group = augroup,
	callback = function()
		vim.highlight.on_yank({
			higroup = "IncSearch",
			timeout = 150,
			on_visual = true,
		})
	end,
})

vim.api.nvim_create_autocmd("CmdlineEnter", {
	group = augroup,
	pattern = { "/", "?" },
	callback = function()
		vim.opt_global.hlsearch = true
	end,
})

vim.api.nvim_create_autocmd("CmdlineLeave", {
	group = augroup,
	pattern = { "/", "?" },
	callback = function()
		vim.opt_global.hlsearch = false
	end,
})

local filetype_handlers = {
	[{
		"markdown",
		"python",
		"json",
		"javascript",
		"javascriptreact",
		"typescript",
		"typescriptreact",
		"html",
		"css",
		"scss",
		"php",
	}] = function()
		vim.opt_local.expandtab = true
		vim.opt_local.shiftwidth = 0
		vim.opt_local.tabstop = 4
		vim.opt_local.softtabstop = 4
	end,

	qf = function()
		vim.opt_local.list = false
		vim.opt_local.statusline = statuslines.active
	end,

	NeogitStatus = function()
		vim.opt_local.list = false
	end,
}

for pattern, callback in pairs(filetype_handlers) do
	vim.api.nvim_create_autocmd("FileType", {
		group = augroup,
		pattern = pattern,
		callback = callback,
	})
end
-- }}}

-- colorscheme and highlights {{{
vim.api.nvim_create_autocmd("ColorScheme", {
	group = augroup,
	pattern = "*",
	callback = function()
		vim.cmd([[
      highlight Normal             ctermbg=NONE guibg=NONE
      highlight NormalNC           ctermbg=NONE guibg=NONE
      highlight CursorLine         ctermbg=8    guibg=#282a2b
      highlight TrailingWhitespace ctermbg=8    guibg=#41535B ctermfg=0    guifg=Black
      highlight VertSplit          ctermbg=NONE guibg=NONE    ctermfg=Gray guifg=Gray
      highlight StatusLine         ctermbg=8    guibg=#313131 ctermfg=15   guifg=#cccccc
      highlight StatusLineNC       ctermbg=0    guibg=#313131 ctermfg=8    guifg=#999999
      highlight StatusLineSection  ctermbg=8    guibg=#55b5db ctermfg=0    guifg=#333333
      highlight StatusLineSectionV ctermbg=11   guibg=#a074c4 ctermfg=0    guifg=#000000
      highlight StatusLineSectionI ctermbg=10   guibg=#9fca56 ctermfg=0    guifg=#000000
      highlight StatusLineSectionC ctermbg=12   guibg=#db7b55 ctermfg=0    guifg=#000000
      highlight StatusLineSectionR ctermbg=12   guibg=#ed3f45 ctermfg=0    guifg=#000000
      highlight StatusLineLspError ctermbg=8    guifg=#313131              guibg=#ff0000
      highlight StatusLineLspWarn  ctermbg=8    guifg=#313131              guibg=#ff8800
      highlight StatusLineLspInfo  ctermbg=8    guifg=#313131              guibg=#2266cc
      highlight StatusLineLspHint  ctermbg=8    guifg=#313131              guibg=#d6d6d6
    ]])
	end,
})

vim.cmd.colorscheme("base16-seti")
-- }}}

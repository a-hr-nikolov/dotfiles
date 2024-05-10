# dotfiles

This is a personal, but public repository for most of my dotfiles and related configuration details.

You can learn more about the concept here:

- [dotfiles.github.io](https://dotfiles.github.io/)
- [Awesome Dotfiles](https://github.com/webpro/awesome-dotfiles)

## Structure

The purpose of the dotfiles structure is to be compatible with `~/` and `~/.config`. Because of this the `dotfiles` repository can be considered `~/`, and every file directly in it can be symlinked. Symlinking directories is not advised. That is because if `dotfiles/config` is symlinked as `~/.config` it will get filled with all kinds of unnecessary distro-related files.

Because of the above, I will probably write a script that populates `~/.config` with whatever is in `dotfiles/.config` with the following rules:

- Directories are created at their respective places (e.g. `dotfiles/.config/fish` will not be symlinked, but rather a new directory will be created (if it doesn't exist) as `~/.config/fish`).
- Files are symlinked (i.e. the newly created directories will be filled mostly (or entirely) with symlinks).

This will also help avoid unnecessary clutter in `dotfiles/.config/<dir>`, as some programs save quite a lot of irrelevant files in their respective config dirs.

## Nix?

Nix provides a slightly different way to manage configuration through Home Manager. Since I am planning on hopping to NixOS at some point, I am mainly writing this as a reminder to check whether I can keep one `dotfiles` repository, which can be used for other distros and Nix at the same time.

%global tl_name plex-otf
%global tl_revision 79300

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.12
Release:	%{tl_revision}.1
Summary:	Support for the OpenType font IBM Plex
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/plex-otf
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/plex-otf.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/plex-otf.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package supports the free otf fonts from the IBM Plex project which
are available from GitHub or already part of your system
(Windows/Linux/...). This package supports only XeLaTeX or LuaLaTeX; for
pdfLaTeX use plex-mono.sty, plex-sans.sty, and/or plex-serif.sty from
the plex package.


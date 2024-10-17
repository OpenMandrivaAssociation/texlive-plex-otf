Name:		texlive-plex-otf
Version:	68238
Release:	1
Summary:	Support for the OpenType font IBM Plex
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/plex-otf
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plex-otf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plex-otf.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package supports the free otf fonts from the IBM Plex
project which are available from GitHub or already part of your
system (Windows/Linux/...). This package supports only XeLaTeX
or LuaLaTeX; for pdfLaTeX use plex-mono.sty, plex-sans.sty,
and/or plex-serif.sty from the plex package. IBM Plex has no
math symbols. You will have to use one of the existing math
fonts if you need them.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/plex-otf
%doc %{_texmfdistdir}/doc/fonts/plex-otf

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

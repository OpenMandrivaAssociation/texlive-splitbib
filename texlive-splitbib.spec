%global tl_name splitbib
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.17
Release:	%{tl_revision}.1
Summary:	Split and reorder your bibliography
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/splitbib
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/splitbib.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/splitbib.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/splitbib.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package enables you to split a bibliography into several categories
and subcategories. It does not depend on BibTeX: any bibliography may be
split and reordered.


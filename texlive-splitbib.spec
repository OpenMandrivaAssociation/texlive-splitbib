Name:		texlive-splitbib
Version:	15878
Release:	2
Summary:	Split and reorder your bibliography
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/splitbib
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/splitbib.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/splitbib.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/splitbib.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package enables you to split a bibliography into several
categories and subcategories. It does not depend on BibTeX: any
bibliography may be split and reordered.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/splitbib/splitbib.sty
%doc %{_texmfdistdir}/doc/latex/splitbib/README
%doc %{_texmfdistdir}/doc/latex/splitbib/splitbib.pdf
#- source
%doc %{_texmfdistdir}/source/latex/splitbib/splitbib.dtx
%doc %{_texmfdistdir}/source/latex/splitbib/splitbib.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

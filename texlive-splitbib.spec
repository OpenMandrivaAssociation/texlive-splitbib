# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/splitbib
# catalog-date 2007-01-15 00:27:07 +0100
# catalog-license lppl
# catalog-version 1.17
Name:		texlive-splitbib
Version:	1.17
Release:	1
Summary:	Split and reorder your bibliography
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/splitbib
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/splitbib.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/splitbib.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/splitbib.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package enables you to split a bibliography into several
categories and subcategories. It does not depend on BibTeX: any
bibliography may be split and reordered.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/splitbib
# catalog-date 2007-01-15 00:27:07 +0100
# catalog-license lppl
# catalog-version 1.17
Name:		texlive-splitbib
Version:	1.17
Release:	2
Summary:	Split and reorder your bibliography
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/splitbib
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/splitbib.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/splitbib.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/splitbib.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.17-2
+ Revision: 756156
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.17-1
+ Revision: 719566
- texlive-splitbib
- texlive-splitbib
- texlive-splitbib
- texlive-splitbib


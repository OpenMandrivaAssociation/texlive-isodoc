# revision 27977
# category Package
# catalog-ctan /macros/latex/contrib/isodoc
# catalog-date 2012-09-29 14:32:13 +0200
# catalog-license lppl
# catalog-version 0.11
Name:		texlive-isodoc
Version:	0.11
Release:	1
Summary:	A LaTeX class for the preparation of letters and invoices
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/isodoc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/isodoc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/isodoc.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/isodoc.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The isodoc class can be used for the preparation of letters and
invoices (and, in the future, similar documents). Documents are
set up with options, thus making the class easily adaptable to
user's wishes and extensible for other document types. The
class is based on Victor Eijkhout's NTG brief class, which
implements the NEN1026 standard.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/isodoc/isodoc.cls
%{_texmfdistdir}/tex/latex/isodoc/isodocsymbols.sty
%doc %{_texmfdistdir}/doc/latex/isodoc/README
%doc %{_texmfdistdir}/doc/latex/isodoc/accept.tex
%doc %{_texmfdistdir}/doc/latex/isodoc/binaries.m64
%doc %{_texmfdistdir}/doc/latex/isodoc/inst
%doc %{_texmfdistdir}/doc/latex/isodoc/invoice.tex
%doc %{_texmfdistdir}/doc/latex/isodoc/isodoc.pdf
%doc %{_texmfdistdir}/doc/latex/isodoc/isontg.sty
%doc %{_texmfdistdir}/doc/latex/isodoc/isowybo.sty
%doc %{_texmfdistdir}/doc/latex/isodoc/language_template.tex
%doc %{_texmfdistdir}/doc/latex/isodoc/letter.tex
%doc %{_texmfdistdir}/doc/latex/isodoc/listkeys
%doc %{_texmfdistdir}/doc/latex/isodoc/logoletter.tex
%doc %{_texmfdistdir}/doc/latex/isodoc/logostyle.sty
%doc %{_texmfdistdir}/doc/latex/isodoc/ltxdoc.cfg
%doc %{_texmfdistdir}/doc/latex/isodoc/mystyle.sty
%doc %{_texmfdistdir}/doc/latex/isodoc/ntgletter.tex
%doc %{_texmfdistdir}/doc/latex/isodoc/typo
#- source
%doc %{_texmfdistdir}/source/latex/isodoc/isodoc.dtx
%doc %{_texmfdistdir}/source/latex/isodoc/isodoc.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

# revision 19617
# category Package
# catalog-ctan /macros/latex/contrib/isodoc
# catalog-date 2010-08-25 10:26:17 +0200
# catalog-license lppl
# catalog-version 0.8
Name:		texlive-isodoc
Version:	0.8
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The isodoc class can be used for the preparation of letters and
invoices (and, in the future, similar documents). Documents are
set up with options, thus making the class easily adaptable to
user's wishes and extensible for other document types. The
class is based on Victor Eijkhout's NTG brief class, which
implements the NEN1026 standard.

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
%{_texmfdistdir}/tex/latex/isodoc/isodoc.cls
%doc %{_texmfdistdir}/doc/latex/isodoc/Entries
%doc %{_texmfdistdir}/doc/latex/isodoc/README
%doc %{_texmfdistdir}/doc/latex/isodoc/Repository
%doc %{_texmfdistdir}/doc/latex/isodoc/Root
%doc %{_texmfdistdir}/doc/latex/isodoc/accept.tex
%doc %{_texmfdistdir}/doc/latex/isodoc/binaries.m64
%doc %{_texmfdistdir}/doc/latex/isodoc/doc/letter.tex
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
%doc %{_texmfdistdir}/source/latex/isodoc/isodoc_letterpaper.dtx
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}

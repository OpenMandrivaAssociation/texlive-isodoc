# revision 33075
# category Package
# catalog-ctan /macros/latex/contrib/isodoc
# catalog-date 2014-03-01 23:31:16 +0100
# catalog-license lppl1.3
# catalog-version 1.04
Name:		texlive-isodoc
Version:	1.04
Release:	2
Summary:	A LaTeX class for typesetting letters and invoices
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/isodoc
License:	LPPL1.3
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
class is based on the NTG brief class by Victor Eijkhout, which
implements the NEN1026 standard.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/isodoc/isodoc-ca-ES.ldf
%{_texmfdistdir}/tex/latex/isodoc/isodoc-de-DE.ldf
%{_texmfdistdir}/tex/latex/isodoc/isodoc-en-GB.ldf
%{_texmfdistdir}/tex/latex/isodoc/isodoc-en-US.ldf
%{_texmfdistdir}/tex/latex/isodoc/isodoc-es-ES.ldf
%{_texmfdistdir}/tex/latex/isodoc/isodoc-fr-FR.ldf
%{_texmfdistdir}/tex/latex/isodoc/isodoc-it-IT.ldf
%{_texmfdistdir}/tex/latex/isodoc/isodoc-nb-NO.ldf
%{_texmfdistdir}/tex/latex/isodoc/isodoc-nl-BE.ldf
%{_texmfdistdir}/tex/latex/isodoc/isodoc-nl-NL.ldf
%{_texmfdistdir}/tex/latex/isodoc/isodoc-sr-RS.ldf
%{_texmfdistdir}/tex/latex/isodoc/isodoc.cls
%doc %{_texmfdistdir}/doc/latex/isodoc/README
%doc %{_texmfdistdir}/doc/latex/isodoc/accept/accept.sty
%doc %{_texmfdistdir}/doc/latex/isodoc/accept/accept.tex
%doc %{_texmfdistdir}/doc/latex/isodoc/accept/acceptform.jpg
%doc %{_texmfdistdir}/doc/latex/isodoc/accept/ntgcolor.png
%doc %{_texmfdistdir}/doc/latex/isodoc/inst
%doc %{_texmfdistdir}/doc/latex/isodoc/invoice/invoice.sty
%doc %{_texmfdistdir}/doc/latex/isodoc/invoice/invoice.tex
%doc %{_texmfdistdir}/doc/latex/isodoc/isodoc.pdf
%doc %{_texmfdistdir}/doc/latex/isodoc/letter/letter.sty
%doc %{_texmfdistdir}/doc/latex/isodoc/letter/letter.tex
%doc %{_texmfdistdir}/doc/latex/isodoc/letter/sign.png
%doc %{_texmfdistdir}/doc/latex/isodoc/letter/signmarked.png
%doc %{_texmfdistdir}/doc/latex/isodoc/listkeys
%doc %{_texmfdistdir}/doc/latex/isodoc/logoletter/ChopinScript.ttf
%doc %{_texmfdistdir}/doc/latex/isodoc/logoletter/logoletter.sty
%doc %{_texmfdistdir}/doc/latex/isodoc/logoletter/logoletter.tex
%doc %{_texmfdistdir}/doc/latex/isodoc/logoletter/shiva-shakti.png
%doc %{_texmfdistdir}/doc/latex/isodoc/logoletter/signblue.png
%doc %{_texmfdistdir}/doc/latex/isodoc/logoletter/typo.txt
%doc %{_texmfdistdir}/doc/latex/isodoc/ntgletter/ntgcolor.png
%doc %{_texmfdistdir}/doc/latex/isodoc/ntgletter/ntgletter.sty
%doc %{_texmfdistdir}/doc/latex/isodoc/ntgletter/ntgletter.tex
%doc %{_texmfdistdir}/doc/latex/isodoc/ntgletter/signlong.png
%doc %{_texmfdistdir}/doc/latex/isodoc/ntgletter/signshort.png
%doc %{_texmfdistdir}/doc/latex/isodoc/template.ldf
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

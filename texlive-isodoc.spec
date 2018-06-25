Name:		texlive-isodoc
Version:	1.10
Release:	1
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
%{_texmfdistdir}/tex/latex/isodoc
%doc %{_texmfdistdir}/doc/latex/isodoc
#- source
%doc %{_texmfdistdir}/source/latex/isodoc

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

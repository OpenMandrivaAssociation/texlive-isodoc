%global tl_name isodoc
%global tl_revision 75787

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.16
Release:	%{tl_revision}.1
Summary:	A LaTeX class for typesetting letters and invoices
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/isodoc
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/isodoc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/isodoc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/isodoc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The isodoc class can be used for the preparation of letters and invoices
(and, in the future, similar documents). Documents are set up with
options, thus making the class easily adaptable to user's wishes and
extensible for other document types. The class is based on the NTG brief
class by Victor Eijkhout, which implements the NEN1026 standard.


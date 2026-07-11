%global tl_name latex2e-help-texinfo
%global tl_revision 79327

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Unofficial reference manual covering LaTeX2e
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/latex2e-help-texinfo
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex2e-help-texinfo.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex2e-help-texinfo.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The manual is provided as Texinfo source (which was originally derived
from the VMS help file in the DECUS TeX distribution of 1990, with many
subsequent changes). This is a collaborative development, and details of
getting involved are to be found on the package home page. A Spanish
translation is included here, and a French translation is available as a
separate package. All the other formats in the distribution are derived
from the Texinfo source, as usual.


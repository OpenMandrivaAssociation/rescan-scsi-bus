Summary:	Rescan SCSI bus in Linux
Name:		rescan-scsi-bus
Version:	1.56
Release:	1
License:	GPL
Group:		System/Kernel and hardware 
Source0:	http://www.garloff.de/kurt/linux/%{name}.sh
URL:		http://www.garloff.de/kurt/linux/
BuildArch:	noarch

%description
Linux allows you to add and remove SCSI devices without rebooting by
using the

echo "scsi add-single-device H C I L" > /proc/scsi/scsi

command (H = host, C = channel, I = SCSI ID, L = SCSI LUN). The
remove-single-device command works similarily.

Note, however, that the SCSI bus was NOT designed for hot-plugging, so
you might be out of luck... And you have to be sure, that termination
is OK. All filesystems on a device have to be unmounted before
disconnecting it or powering it down.

%prep
%setup -q -c -T
install %{SOURCE0} %{name}

%install
install -d %buildroot%{_sbindir}
install %{name} %buildroot%{_sbindir}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/rescan-scsi-bus


%changelog
* Tue Feb 14 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.56-1
+ Revision: 773933
- imported package rescan-scsi-bus


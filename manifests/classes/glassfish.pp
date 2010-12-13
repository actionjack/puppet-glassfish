# Class: glassfish
#
# This class manages the glassfish java application server
#
# Parameters:
#   None
#
# Actions:
#   Installs and configures the glassfish application server
#
# Requires:
#   - Package["glassfish"]
#
# Sample Usage:
#
class glassfish::install {
    $packagelist = ["glassfish"]
    package{ $packagelist: ensure => installed }
}

class glassfish::absent {
    $packagelist = ["glassfish"]
    package{ $packagelist: ensure => absent }
}
 
class glassfish::config {
    File{
        require => Class["glassfish::install"],
        notify  => Class["glassfish::service"],
        owner   => "root",
        group   => "root",
        mode    => 644
    }
}
 
class glassfish::service {
    service{"glassfish":
        ensure  => running,
        enable  => true,
        require => Class["glassfish::config"],
    }
}

class glassfish::disableboot {
    service{"glassfish":
	enable  => false
    }
}

 
class glassfish {
    include glassfish::install, 
	    glassfish::config, 
	    glassfish::service
}

class glassfish::disable {
    include glassfish::install,
            glassfish::config,
	    glassfish::disableboot
}

class glassfish::monitor {
#noop not in use at the moment
}

class glassfish::backup {
#noop not in use at the moment
}

<?php
require_once('plugins/login-servers.php');

/** Set supported servers
    * @param array array($domain) or array($domain => $description) or array($category => array())
    * @param string
    */
return new AdminerLoginServers(
    [
        "MySQL" => array( "server" =>"mysql", "driver"=> "server" ),
        "PostgreSQL" => array( "server" =>"postgres", "driver"=> "pgsql" )
    ]
);
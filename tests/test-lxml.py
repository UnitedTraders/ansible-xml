from lxml import etree
import lxml.html
from StringIO import StringIO

f = StringIO('''\
<?xml version='1.0' encoding='UTF-8'?>
<server xmlns="urn:jboss:domain:4.0">
    <profile>
        <subsystem xmlns="urn:jboss:domain:logging:3.0">
            <console-handler name="CONSOLE">
                <level name="INFO"/>
                <formatter>
                    <named-formatter name="COLOR-PATTERN"/>
                </formatter>
            </console-handler>
        </subsystem>
        <subsystem xmlns="urn:jboss:domain:deployment-scanner:2.0">
            <deployment-scanner path="deployments" relative-to="jboss.server.base.dir" scan-interval="5000" runtime-failure-causes-rollback="${jboss.deployment.scanner.rollback.on.failure:false}"/>
        </subsystem>
        <subsystem xmlns="urn:jboss:domain:bean-validation:1.0"/>
        <subsystem xmlns="urn:jboss:domain:keycloak-server:1.1">
            <web-context>auth</web-context>
            <spi name="realm">
                <default-provider>jpa</default-provider>
            </spi>
            <spi name="connectionsHttpClient">
                <provider name="default" enabled="true"/>
            </spi>
            <spi name="emailTemplate">
                <default-provider>aurora-email-template-factory</default-provider>
            </spi>
        </subsystem>
    </profile>
</server>
''')

doc = etree.parse(f)

r = doc.xpath("//d:spi[@name=\"emailTemplate\"]", namespaces={'d': 'urn:jboss:domain:keycloak-server:1.1'})

print(r[0].tag)
print(r[0].text)
print(lxml.html.tostring(r[0]))
# OCP Meeting

Date: 2022-07-01

Things that will need to be built:

1. Will need to build some vault access for all environment variables/secrets
2. Will need to integrate JWT v3.0
3. Will need to upgrade neo4j to v4.3 (maybe later)
4. Will need to play with 
5. HTTP PRoxy/AWS Load Balancer
6. Interacts with Kubelets (load balancer services, Kubernetes config)
7. Figure out Login/LDAP/MFA
8. 


Rules and firewalls will need access to onpremise neo4j (full connectivity between)
Do we plan to move neo4j to amazon?

May need to bring in additional application teams for neo4
Can mount NAS to container and write data to it, just have to make sure that we have permissions
and write it as correct ids, but that's standard that would restrict us from doing so

If writing files, make sure that we use certain user

Artifactory Container Registry

Normal Order:
- Jenkins builds image
- Push to Artifactory
- OCP Deploy 



Questions:
1. Do we have to integrate code base into DFS Github since it's our proprietary code? (CI/CD team to ask)
2. Is there any issues with integration with 
3. How big containers? Pod size is average 2g to 4g of memory, cores is weird (ghz used) 1 to 2 cores
4. 


Next Steps:

1. Request access to labs
2. Open quick ticket in OCP 

This is the location of all the deployment files that I have made so far. I have a deployment for the storefront, dashboard, and core. I also created seperate deployment files for pgadmin and postgres. 

I had the pgadmin and postgres running through an external service with nodeport but have recently removed it. My goal is to handle all out side connections with nginx and ingress. I have my attempt of created an ingress controller in the ingress controller folder if you would like to take a look at it. 

I have attempted at configuring ingress for storefront at the moment. I have the storefront ingress file made and had changed my host file on my local computer to set up the braingustorefront.com url. 

1. start a minikube cluster
2. enable minikube ingress-controller "minikube addons enable ingress"
Still working on the ingress controller file. It is a practice file that I was working one.

The actual ingress-controller can be found in ingress/controller/nginx. That controller works fine if you do not have minikube installed.

3. apply the ingress file
4. apply any of the deployment files for testing.

I wish to be able to see the storefront in the browser.

example in  my /etc/host file I have: 192.17.41.14   braingustorefront.com



Any help would be greatly appreciated thank you!!!


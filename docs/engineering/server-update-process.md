# Server update process

## Updating the Demo server

- Create a new server on gcp which will be used as a template for a demo server. we will call it as `demo-template`
- Deploy a new demo server using ansible.
- Create a snapshot of the demo server you created by visiting the [snapshot page](https://console.cloud.google.com/compute/snapshots?project=mathesar). This page should be on the navigation panel on the left and can be under "Storage -> Snapshots". Configure the following options
    - Set the name to `live-demo-v{deployed-version}`
    - Set the source disk as the `demo-template` server you created
- Create an image based on the created snapshot by visiting the [Images page](https://console.cloud.google.com/compute/imagesAdd?project=mathesar). This page should be on the navigation panel on the left and can be under "Storage -> Images".
    - Set the name to `live-demo-v{deployed-version}`
    - Set the source as `Snapshot`
    - Set the source disk as the source snapshot `live-demo-v{deployed-version}`
- Edit the load balancer instance group by visiting the [instance group page](https://console.cloud.google.com/compute/instanceGroups/edit/us-central1-a/live-demo-server?project=mathesar)
  - On that same page, create a new instance template by clicking on "Instance template" dropdown under "Instances" and click on "Create new instance template"
  - On the right-hand side, the instance template creation menu will open up. Set the following configurations
    - Set the name of the template as `live-demo-v{deployed-version}`
    - Set the machine type as "e2-Standard-2"
    - Set the boot disk to the image you created before by
      - Click on the "Change" button under the "Boot disk" section
      - Click on the "Custom Images" tab in the popup that appears
        - Set the image to `live-demo-v{deployed-version}` which you created earlier
      - Click save, and you will be taken back to the instance template creation popup
    - Tick the following firewall options in the firewall section
      - Allow HTTP traffic
      - Allow HTTPS traffic
    - Click on save to create a new instance template
  - Select the instance template you created now
  - Hit save
  - In the [Instance group page](https://console.cloud.google.com/compute/instanceGroups/details/us-central1-a/live-demo-server?project=mathesar), click on "Update VMs"
    - Choose the template `live-demo-v{deployed-version}` you created
    - Click on Update VMs
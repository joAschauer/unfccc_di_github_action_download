# unfccc_di_github_action_download

Uses github actions to download data from the UNFCCC data interface.

This repository provides a workflow which downloads all data from the UNFCCC
[flexible query API](https://di.unfccc.int/flex_annex1) and saves it to a single file.
The download is done with the [UNFCCC DI API](https://github.com/pik-primap/unfccc_di_api)
python package.

You can trigger a download by mannually running the workflow `download` above in
"Actions" tab. Read the [Github docs on how to manually run a workflow](https://docs.github.com/de/actions/
using-workflows/manually-running-a-workflow). The downloaded data is stored in
a job artifact of the github workflow. 
[See here how to download workflow artifacts](https://docs.github.com/en/actions/managing-workflow-runs/downloading-workflow-artifacts).

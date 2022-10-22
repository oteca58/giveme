const containerActivities = document.querySelector(".activities");

const showActivity = async function () {
  try {
    const res = await fetch("http://127.0.0.1:8000/api/v1/activities/");
    const data = await res.json();

    if (!res.ok) throw new Error(`${data.message} (${res.status})`);

    //let { activity } = data[0];
    // let { activity } = data;
    // activity = {
    //   description: activity.description,
    //   client_code: activity.client_code,
    //   due_date: activity.due_date,
    //   assignment: activity.assignment,
    //   status: activity.status,
    //   effort: activity.effort,
    //   billable_to: activity.billable_to,
    //   invoiced: activity.invoiced,
    // };
    //console.log(activity);
    //const markup = `<h1> ${activity.id}</h1>`;

    const markup = data
      .map((activity, index) => {
        return `<tr>
        <td class="column1">${activity.id}</td>
        <td class="column2">${activity.description}</td>
        <td class="column3">${activity.client_code}</td>
        <td class="column4">${activity.due_date}</td>
        <td class="column5">${activity.assignment}</td>
        <td class="column6">${activity.status}</td>
        <td class="column7">${activity.effort}</td>
        <td class="column8">${activity.billable_to}</td>
        <td class="column9">${activity.invoiced}</td></tr>`;
      })

      .join("");
    containerActivities.insertAdjacentHTML("afterbegin", markup);
  } catch (err) {
    console.log(err);
  }
};

showActivity();

const filterCompletedActivity = async function () {
  try {
    const res = await fetch(
      "http://127.0.0.1:8000/api/v1/activities/?search=COMPLETED"
    );
    const data = await res.json();
    console.log(data);
    const markup = data
      .map((activity, index) => {
        return `<tr>
    <td class="column1">${activity.id}</td>
    <td class="column2">${activity.description}</td>
    <td class="column3">${activity.client_code}</td>
    <td class="column4">${activity.due_date}</td>
    <td class="column5">${activity.assignment}</td>
    <td class="column6">${activity.status}</td>
    <td class="column7">${activity.effort}</td>
    <td class="column8">${activity.billable_to}</td>
    <td class="column9">${activity.invoiced}</td></tr>`;
      })
      .join("");
    containerActivities.innerHTML = markup;
  } catch (err) {
    console.log(err);
  }
};

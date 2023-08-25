document.addEventListener('DOMContentLoaded', () => {
    const signinForm = document.getElementById('signin-form');
    const visitorDetailsForm = document.getElementById('visitor-details-form');
    const staffMemberInput = document.getElementById('staff-member');
    const staffMemberList = document.getElementById('staff-member-list');
    const drinkSelect = document.getElementById('drink');
    const drinkRequestForm = document.getElementById('drink-request-form');
    const thankYouScreen = document.getElementById('thank-you-screen');
    const representativeName = document.getElementById('representative-name');
    const selectedDrink = document.getElementById('selected-drink');

    signinForm.addEventListener('submit', async (event) => {
        event.preventDefault();

        const name = document.getElementById('name').value;
        const mobile = document.getElementById('mobile').value;
        const address = document.getElementById('address').value;

        const response = await fetch('/api/sign_in/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, mobile, address }),
        });

        if (response.status === 201) {
            alert('Sign-in successful!');
            signinForm.reset();
        } else {
            alert('Sign-in failed. Please try again.');
        }
    });
});

    staffMemberInput.addEventListener('input', async () => {
        const searchQuery = staffMemberInput.value;
        const response = await fetch(`/api/get_staff_members/?search=${searchQuery}`);
        const staffMembers = await response.json();

        staffMemberList.innerHTML = '';
        staffMembers.forEach((staffMember) => {
            const listItem = document.createElement('li');
            listItem.textContent = staffMember.name;
            staffMemberList.appendChild(listItem);
        });
    });

    visitorDetailsForm.addEventListener('submit', async (event) => {
        event.preventDefault();

        const staffMemberName = staffMemberInput.value;
        const staffMember = staffMembers.find((member) => member.name === staffMemberName);

        if (!staffMember) {
            alert('Please select a valid staff member.');
            return;
        }

        const reason = document.getElementById('reason').value;

        const response = await fetch('/api/save_visitor_details/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                staff_member: staffMember.id,
                visitor: 1,  // Replace with the actual visitor ID
                reason,
                state: 'Pending',
            }),
        });

        if (response.status === 201) {
            alert('Visitor details saved successfully.');
            visitorDetailsForm.reset();
        } else {
            alert('Failed to save visitor details. Please try again.');
        }
    });
});

    async function populateDrinks() {
        const response = await fetch('/api/get_drinks/');
        const drinks = await response.json();

        drinkSelect.innerHTML = '';
        drinks.forEach((drink) => {
            const option = document.createElement('option');
            option.value = drink.id;
            option.textContent = drink.name;
            drinkSelect.appendChild(option);
        });
    }

    drinkRequestForm.addEventListener('submit', async (event) => {
        event.preventDefault();

        const selectedDrinkId = drinkSelect.value;
        const selectedDrink = drinkSelect.options[drinkSelect.selectedIndex].text;

        const response = await fetch('/api/save_visitor_drink/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                visitor: 1,  // Replace with the actual visitor ID
                drink: selectedDrinkId,
                state: 'Pending',
            }),
        });

        if (response.status === 201) {
            alert('Drink request submitted successfully.');
            drinkRequestForm.reset();
        } else {
            alert('Failed to submit drink request. Please try again.');
        }
    });

    populateDrinks();
});

// Show the thank-you screen
    function showThankYouScreen(representativeName, selectedDrink) {
        const thankYouScreen = document.getElementById('thank-you-screen');
        const representativeNameSpan = document.getElementById('representative-name');
        const selectedDrinkSpan = document.getElementById('selected-drink');

        representativeNameSpan.textContent = representativeName;
        selectedDrinkSpan.textContent = selectedDrink;

        thankYouScreen.classList.remove('hidden');

        // Redirect back to sign-in screen after 5 minutes
        setTimeout(() => {
            window.location.href = '/';
        }, 5 * 60 * 1000); // 5 minutes in milliseconds
    }
});